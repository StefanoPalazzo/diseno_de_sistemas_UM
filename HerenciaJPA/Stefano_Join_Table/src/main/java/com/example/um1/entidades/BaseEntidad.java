package com.example.um1.entidades;

import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.MappedSuperclass;
import lombok.*;
import lombok.experimental.SuperBuilder;



@MappedSuperclass
// Esta clase no se persiste
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@SuperBuilder

public class BaseEntidad {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    protected Long id;
}
