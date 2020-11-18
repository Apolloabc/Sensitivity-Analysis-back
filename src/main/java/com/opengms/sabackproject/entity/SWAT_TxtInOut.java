package com.opengms.sabackproject.entity;

import lombok.Data;

import java.util.List;

@Data
public class SWAT_TxtInOut extends SA_Project{


    // 待测参数
    List<SWAT_TxtInOut_Param> paramList;

    // 模拟设置
    String simSetting;

    // 采样之后，填充每一组mdlJson，发布计算任务
    Float[][] sampleParams;

    // 模拟结果

    // 敏感性系数结果

    // 参数率定结果

    // 单次模拟参数

    // 单次模拟结果

}
