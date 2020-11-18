package com.opengms.sabackproject.controller;

import com.opengms.sabackproject.entity.SA_Project;
import com.opengms.sabackproject.entity.SWAT_TxtInOut;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/project")
public class ProjectController {

    @RequestMapping(value = "/create",method = RequestMethod.POST)
    public boolean CreateNewProject(@RequestBody SA_Project project){
        System.out.println(project.getName());
        System.out.println(project);
        return true;
    }
}
