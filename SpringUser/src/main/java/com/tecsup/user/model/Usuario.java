package com.tecsup.user.model;

import java.time.LocalDate;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.format.annotation.DateTimeFormat.ISO;

@Entity
@Table(name = "apirest_usuario")
public class Usuario {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	private String nombres;
	private String apellidos;
	
	@Column(length = 8)
	private String dni;
	
	private String correo;
	private String password;
	
	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getNombres() {
		return nombres;
	}

	public void setNombres(String nombres) {
		this.nombres = nombres;
	}

	public String getApellidos() {
		return apellidos;
	}

	public void setApellidos(String apellidos) {
		this.apellidos = apellidos;
	}

	public String getDni() {
		return dni;
	}

	public void setDni(String dni) {
		this.dni = dni;
	}

	public String getCorreo() {
		return correo;
	}

	public void setCorreo(String correo) {
		this.correo = correo;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public Usuario() {
		super();
	}

	public Usuario(Long id, String nombres, String apellidos, String dni, String correo,
			String password) {
		super();
		this.id = id;
		this.nombres = nombres;
		this.dni = dni;
		this.correo = correo;
		this.password = password;

	}

	public Usuario(String nombres, String apellidos, String dni, String correo, String password) {
		super();
		this.nombres = nombres;
		this.apellidos = apellidos;
		this.dni = dni;
		this.correo = correo;
		this.password = password;
	}

	
}
