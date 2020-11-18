package com.opengms.sabackproject.entity;

import lombok.Data;

@Data
public class SWAT_TxtInOut_Param {
    String param_name;
    String description;
    String option_type;
    Float left;
    Float right;
    Float value;
}
