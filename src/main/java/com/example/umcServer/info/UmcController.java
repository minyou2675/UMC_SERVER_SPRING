package com.example.umcServer.info;

import com.example.umcServer.dto.MemberDto;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/user")
public class UmcController {

        @GetMapping("/read")
        public String test(){
            return "Hello world";

        }
        @PostMapping("/post/{variable}")
        public String signup(@PathVariable String variable){
            return variable;
        }
        @GetMapping("/users")
        public String Lookup(){
            MemberDto member = new MemberDto();
            return member.toString();

        }
}
