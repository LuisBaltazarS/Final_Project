package com.tecsup.user.service;

import java.util.ArrayList;
import java.util.Optional;

import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import com.tecsup.user.dto.UserRegisterDTO;
import com.tecsup.user.model.Usuario;
import com.tecsup.user.repository.UserRepository;


@Service
public class UserServiceImpl implements UserService{

	private UserRepository usuarioRepositorio;
	
	public UserServiceImpl(UserRepository usuarioRepositorio) {
		super();
		this.usuarioRepositorio = usuarioRepositorio;
	}

	@Override
	public Usuario save(UserRegisterDTO registroDTO) {
		
		Usuario usuario = new Usuario(registroDTO.getNombres(), registroDTO.getApellidos(), registroDTO.getNacimiento(), 
				registroDTO.getDni(), registroDTO.getCorreo(), registroDTO.getPassword(), registroDTO.getTelefono(), 
				registroDTO.getInstitucionId(), registroDTO.getTipoId(), registroDTO.getTutorId());
		
		return usuarioRepositorio.save(usuario);
		
	}

	@Override
	public ArrayList<Usuario> getAllUser() {
		
		return (ArrayList<Usuario>) usuarioRepositorio.findAll();
		
	}

	@Override
	public Optional<Usuario> getUserById(Long id) {
		
		return usuarioRepositorio.findById(id);
	}

	@Override
	public boolean deleteUser(Long id) {
		
		try {
			
			usuarioRepositorio.deleteById(id);
			return true;
			
		} catch (Exception e) {
			
			return false;
			
		}
		
	}

	@Override
	public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Usuario actualizarUser(UserRegisterDTO registroDTO, long id) {
		
		Usuario usuario = new Usuario(id, registroDTO.getNombres(), registroDTO.getApellidos(), registroDTO.getNacimiento(), 
				registroDTO.getDni(), registroDTO.getCorreo(), registroDTO.getPassword(), registroDTO.getTelefono(), 
				registroDTO.getInstitucionId(), registroDTO.getTipoId(), registroDTO.getTutorId());
		
		return usuarioRepositorio.save(usuario);
		
	}
	
	

}
