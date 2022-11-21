package com.example.demo.src.restaurant.model;

import lombok.*;

@Getter
@Setter
@AllArgsConstructor

public class Restaurant {
    private int restIdx;
    private  String restname;
    private String category;
    private  String address;
    private int left;
}
