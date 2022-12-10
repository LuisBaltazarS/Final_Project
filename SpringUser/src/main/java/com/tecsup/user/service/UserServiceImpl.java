package com.tecsup.user.service;

import org.springframework.stereotype.Service;

import com.tecsup.user.dto.UserRegisterDTO;
import com.tecsup.user.model.Usuario;
import com.tecsup.user.repository.UserRepository;


@Service
public class UserServiceImpl implements UserService{

	private UserRepository usuarioRepositorio;
	
	@Override
	public Usuario save(UserRegisterDTO registroDTO) {
		
		Usuario usuario = new Usuario(registroDTO.getNombres(), registroDTO.getApellidos(), registroDTO.getNacimiento(), 
				registroDTO.getDni(), registroDTO.getCorreo(), registroDTO.getPassword(), registroDTO.getTelefono(), 
				registroDTO.getInstitucionId(), registroDTO.getTipoId(), registroDTO.getTutorId());
		
		return usuarioRepositorio.save(usuario);
		
	}
	
	

}
