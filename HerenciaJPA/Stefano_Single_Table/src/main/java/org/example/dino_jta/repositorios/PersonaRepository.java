package org.example.dino_jta.repositorios;

import org.example.dino_jta.entidades.Persona;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PersonaRepository extends JpaRepository <Persona, Long>{
}
