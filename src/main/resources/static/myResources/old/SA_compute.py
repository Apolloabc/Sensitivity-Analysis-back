import sys
import numpy as np
from SALib.analyze import morris
from SALib.analyze import sobol
from SALib.analyze import fast
from SALib.util import read_param_file
from SALib.test_functions import Ishigami

def compute(target):
  str_si = ""
  if method == "morris": 
    SI = morris.analyze(params, X, Y, print_to_console=True) 
    str_si = 'names,'+','.join(SI['names'])+'\n' + 'mu_star,'+','.join(str('{:.4f}'.format(i)) for i in SI['mu_star'])+'\n' + 'sigma,'+','.join(str('{:.4f}'.format(i)) for i in SI['sigma'])+'\n'
  elif method == "sobol": 
    SI = sobol.analyze(params, Y, calc_second_order=True, print_to_console=True)  
    str_si = 'names,'+','.join(params['names'])+'\n' +'S1,'+','.join(str('{:.4f}'.format(i)) for i in SI['S1'])+'\n' +'ST,'+','.join(str('{:.4f}'.format(i)) for i in SI['ST'])+'\n'
    str_si += 'S2,'
    for i in range(params['num_vars']):
      str_si += ','.join(str('{:.4f}'.format(i)) for i in SI['S2'][i])+'\n,'
  elif method == "fast":
    SI = fast.analyze(params, Y, print_to_console=True) 
    str_si = 'names,'+','.join(SI['names'])+'\n' + 'S1,'+','.join(str('{:.4f}'.format(i)) for i in SI['S1'])+'\n' + 'ST,'+','.join(str('{:.4f}'.format(i)) for i in SI['ST'])+'\n'

  with open(path+'SA_score_'+target+'.csv', 'w') as f:
    f.write(str_si)

path = sys.argv[1]
method = ""
# path = "I:/saProjectData/9778337f-db32-4a8d-9273-13bdd29ea7ce"
if __name__ == '__main__':
  # 读取参数文件
  with open(path+'paramsSum.txt', 'r') as f:
    param_list = f.readlines()

  num_vars = len(param_list)
  names = []
  bounds = []
  for i in range(0, len(param_list)):
    line = param_list[i].rstrip('\n')
    param = line.split(":")
    names.append(param[0])
    nums = param[1].split(",")
    bounds.append([float(nums[0]),float(nums[1])])

  params = {
    'num_vars': num_vars,
    'names': names,
    'groups': None,
    'bounds': bounds
  }

  # 读取模拟方法，模拟目标
  with open(path+'simSetting.txt', 'r') as f:
    sim_list = f.readlines()

  for i in range(0, len(sim_list)):
    line = sim_list[i].rstrip('\n')
    sim = line.split(":")
    if sim[0] == "SAmethod":
      method = sim[1]
    elif sim[0] == "simTargets":
      targets = sim[1].split(',')
        
  # 读取采样文件
  X = np.load(path+"params_sampling.npy")

  # 读取结果索引文件
  with open(path+'resultIndex.txt', 'r') as f:
    result = f.readlines()
  for i in range(0, len(result)):
    line = result[i].rstrip("\n")
    res = line.split(":")
    if res[0] == "resultForSA":
      resultForSA = res[1]
    elif res[0] == "resultIndexs":
      resultIndexs = list(map(int,res[1].split(","))) 
    elif res[0] == "resultForDisplay":
      resultForDisplay = res[1].split(",")

  # 读取结果文件
  total = np.loadtxt(path + resultForSA,delimiter=" ")

  # 计算各个模拟目标的参数敏感性指标
  for i in range(0, len(targets)):
    Y = total[:,resultIndexs[i]]
    compute(targets[i])


