package com.example.um1.repositorios;

import com.example.um1.entidades.Persona;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PersonaRepository extends JpaRepository <Persona, Long>{
}
