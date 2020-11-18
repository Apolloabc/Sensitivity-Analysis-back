package com.opengms.sabackproject.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/")
public class TestController {
    @RequestMapping(value = "/test",method = RequestMethod.POST)
    public String test(String username, String password){
        return username+"你好呀";

    }
}
