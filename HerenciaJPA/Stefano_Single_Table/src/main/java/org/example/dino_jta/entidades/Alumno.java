package org.example.dino_jta.entidades;

import org.example.dino_jta.enumeraciones.Especialidades;
import jakarta.persistence.DiscriminatorValue;
import jakarta.persistence.Entity;
import lombok.*;
import lombok.experimental.SuperBuilder;

@Entity
@NoArgsConstructor
@AllArgsConstructor
@Getter
@ToString
@Setter
@SuperBuilder

public class Alumno extends Persona {
    private int legajo;

    private Especialidades especialidad;
}
