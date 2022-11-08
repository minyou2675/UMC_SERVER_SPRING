package com.example.umcServer.info;

import com.example.umcServer.dto.MemberDto;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/user")
public class UmcController {

        @GetMapping("/read")
        public String test(){
            return "Hello world";

        }
        @PostMapping("/create")
        public String signup(@RequestBody MemberDto member){
            return member.toString();
        }
        @GetMapping("/users")
        public String Lookup(){
            MemberDto member = new MemberDto();
            return member.toString();

        }
        @PutMapping("/update")
        public ResponseEntity<MemberDto> postMemberDto(@RequestBody MemberDto member){
            return ResponseEntity.status(HttpStatus.ACCEPTED).body(member);
        }
        @DeleteMapping("/delete/{variable}")
        public String DeleteVariable(@PathVariable String variable)
        {return variable;}
}
