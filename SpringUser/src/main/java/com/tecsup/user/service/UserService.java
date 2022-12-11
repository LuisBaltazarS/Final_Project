package com.tecsup.user.service;

import java.util.ArrayList;
import java.util.Optional;

import org.springframework.security.core.userdetails.UserDetailsService;

import com.tecsup.user.dto.UserRegisterDTO; 
import com.tecsup.user.model.Usuario;

public interface UserService extends UserDetailsService{
	
	ArrayList<Usuario> getAllUser();
	
	Optional<Usuario> getUserById(Long id);
	
	Usuario save(UserRegisterDTO usuario);
	
	Usuario actualizarUser(UserRegisterDTO usuario, long id);
	
	boolean deleteUser(Long id);

}