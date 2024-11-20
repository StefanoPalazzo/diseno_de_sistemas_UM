package org.example.dino_jta;

import org.example.dino_jta.entidades.Alumno;
import org.example.dino_jta.entidades.Profesor;
import org.example.dino_jta.enumeraciones.Especialidades;
import org.example.dino_jta.enumeraciones.Titulos;
import org.example.dino_jta.repositorios.AlumnoRepository;
import org.example.dino_jta.repositorios.PersonaRepository;
import org.example.dino_jta.repositorios.ProfesorRepository;
import jakarta.transaction.Transactional;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import java.math.BigDecimal;
import java.time.LocalDate;

@SpringBootApplication
public class DinoJtaApplication {

	private static final Logger logger = LoggerFactory.getLogger(DinoJtaApplication.class);

	@Autowired
	private PersonaRepository personaRepository;
	@Autowired
	private ProfesorRepository profesorRepository;

	@Autowired
	private AlumnoRepository alumnoRepository;
	public static void main(String[] args) {
		SpringApplication.run(DinoJtaApplication.class, args);

		System.out.println("funcionando");
	}




	@Bean
	@Transactional
	CommandLineRunner init(PersonaRepository personaRepository,
						   AlumnoRepository alumnoRepository,
						   ProfesorRepository profesorRepository) {
		return args -> {
			// Creo un objeto alumno
			Profesor pro1 = Profesor.builder()
					.nombre("Alberto")
					.apellido("Cortez")
					.fechaIngreso(LocalDate.of(2022, 1, 1))
					.cantHijos(2)
					.titulo(Titulos.MASTER)
					.sueldo(new BigDecimal("123.45"))
					.build();

			// Lo grabo a través del repositorio de Spring
	profesorRepository.save(pro1);

			Profesor pro2 = Profesor.builder()
					.nombre("NotAlberto")
					.nombre("Cortez")
					.fechaIngreso(LocalDate.of(2022, 1, 1))
					.cantHijos(2)
					.titulo(Titulos.MASTER)
					.sueldo(new BigDecimal("123.45"))
					.build();


			// Lo grabo a través del repositorio de Spring
			profesorRepository.save(pro2);

			Alumno al1 = Alumno.builder()
					.nombre("Dino")
					.apellido("Meschini")
					.legajo(62000)
					.especialidad(Especialidades.BACHILLER)
					.build();

			// Lo grabo a través del repositorio de Spring
			alumnoRepository.save(al1);

			Alumno al2 = Alumno.builder()
					.nombre("Dinon't")
					.apellido("Meschini")
					.legajo(62001)
					.especialidad(Especialidades.BACHILLER)
					.build();

			// Lo grabo a través del repositorio de Spring
			alumnoRepository.save(al2);

			Alumno al3 = Alumno.builder()
					.nombre("Alan")
					.apellido("Turing")
					.legajo(1)
					.especialidad(Especialidades.BACHILLER)
					.build();

			// Lo grabo a través del repositorio de Spring
			alumnoRepository.save(al3);









		};

	};




}
