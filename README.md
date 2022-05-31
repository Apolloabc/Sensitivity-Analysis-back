# Sensitivity-Analysis-back
> The Back-end Sensitivity Analysis module in OpenGMS

```js
|-- src main
    |-- java com opengms sabackproject
    |   |-- controller	// 接口层
    |       |-- ComputableModelController // 计算模型条目上传和获取
    |       |-- DataManagerController // 模型数据上传
    |       |-- ExperienceLibraryController // 知识库上传和获取
    |       |-- ProjectController // 项目创建和获取
    |       |-- SimulationController // SA流程的所有接口：采样、运行、模拟结果、计算Obj、计算SA。检验由前端JS实现。
    |   |-- service		// 服务层
    |       |-- ComputableModelService
    |       |-- ExperienceLibraryService
    |       |-- ProjectService
    |       |-- SimulationService
    |   |-- dao			// 数据层
    |       |-- ComputableModelDao
    |       |-- ExperienceLibraryDao
    |       |-- ProjectDao
    |       |-- SimulationDao
    |       |-- TaskDao
    |   |-- **
    |-- resources 
    |   |-- application.properties // 后台项目的所有静态配置
    |   |-- static myResources // 由SimulationController的接口来调用
    |       |-- OGMS_SALibrary 
    |       |-- params_sampling.py // 参数采样统一入口
    |       |-- extract_result_SWAT(TxtInOut).py // 模拟结果提取
    |       |-- Obj_compute.py // 目标函数计算
    |       |-- SA_compute.py // 敏感性计算
    |       |-- **
    |-- README.md
```