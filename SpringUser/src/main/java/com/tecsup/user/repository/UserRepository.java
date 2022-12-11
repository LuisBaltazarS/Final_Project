package com.tecsup.user.repository;

import org.springframework.data.jpa.repository.JpaRepository; 
import org.springframework.stereotype.Repository;

import com.tecsup.user.model.Usuario;

@Repository
public interface UserRepository extends JpaRepository<Usuario, Long>{

	public Usuario findByCorreo(String correo);
	
}


