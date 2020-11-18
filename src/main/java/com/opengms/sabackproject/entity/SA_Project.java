package com.opengms.sabackproject.entity;

import lombok.Data;

@Data
public class SA_Project {
    String name;
    String description;
    String modelName;

    // 数据和参数都在mdl里
    String mdl;
    Object mdlJson;
}
