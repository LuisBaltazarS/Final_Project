package com.tecsup.user.dto;

import java.util.Date;

public class UserRegisterDTO {

	private Long id;
	private String nombres;
	private String apellidos;
	private Date nacimiento;
	private String dni;
	private String correo;
	private String password;
	private String telefono;
	private int institucionId;
	private int tipoId;
	private int tutorId;

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

	public Date getNacimiento() {
		return nacimiento;
	}

	public void setNacimiento(Date nacimiento) {
		this.nacimiento = nacimiento;
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

	public String getTelefono() {
		return telefono;
	}

	public void setTelefono(String telefono) {
		this.telefono = telefono;
	}

	public int getInstitucionId() {
		return institucionId;
	}

	public void setInstitucionId(int institucionId) {
		this.institucionId = institucionId;
	}

	public int getTipoId() {
		return tipoId;
	}

	public void setTipoId(int tipoId) {
		this.tipoId = tipoId;
	}

	public int getTutorId() {
		return tutorId;
	}

	public void setTutorId(int tutorId) {
		this.tutorId = tutorId;
	}

	public UserRegisterDTO(Long id, String nombres, String apellidos, Date nacimiento, String dni, String correo,
			String password, String telefono, int institucionId, int tipoId, int tutorId) {
		super();
		this.id = id;
		this.nombres = nombres;
		this.apellidos = apellidos;
		this.nacimiento = nacimiento;
		this.dni = dni;
		this.correo = correo;
		this.password = password;
		this.telefono = telefono;
		this.institucionId = institucionId;
		this.tipoId = tipoId;
		this.tutorId = tutorId;
	}

	public UserRegisterDTO(String nombres, String apellidos, Date nacimiento, String dni, String correo,
			String password, String telefono, int institucionId, int tipoId, int tutorId) {
		super();
		this.nombres = nombres;
		this.apellidos = apellidos;
		this.nacimiento = nacimiento;
		this.dni = dni;
		this.correo = correo;
		this.password = password;
		this.telefono = telefono;
		this.institucionId = institucionId;
		this.tipoId = tipoId;
		this.tutorId = tutorId;
	}

	public UserRegisterDTO() {
		super();
	}
	
}
