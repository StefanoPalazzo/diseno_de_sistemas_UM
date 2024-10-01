package org.example.dino_jta.repositorios;

import org.example.dino_jta.entidades.Alumno;
import org.springframework.data.jpa.repository.JpaRepository;

public interface AlumnoRepository extends JpaRepository <Alumno, Long> {
}
