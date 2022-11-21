package com.example.demo.src.user.model;

import lombok.*;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor

public class DeleteUserReq {
    private String email;
    private String password;
    private int left;
}
