package com.tecsup.user.service;

import java.util.ArrayList;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

import com.tecsup.user.dto.UserRegisterDTO;
import com.tecsup.user.model.Usuario;
import com.tecsup.user.repository.UserRepository;

@Service
public class UserServiceImpl implements UserService {

	@Autowired
	private BCryptPasswordEncoder passwordEncoder;

	private UserRepository usuarioRepositorio;

	public UserServiceImpl(UserRepository usuarioRepositorio) {
		super();
		this.usuarioRepositorio = usuarioRepositorio;
	}

	@Override
	public Usuario save(UserRegisterDTO registroDTO) {

		Usuario usuario = new Usuario(registroDTO.getNombres(), registroDTO.getApellidos(),
				registroDTO.getDni(), registroDTO.getCorreo(), registroDTO.getPassword());

		
		
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

		Usuario usuario = usuarioRepositorio.findByCorreo(username);

		if (usuario == null) {

			throw new UsernameNotFoundException("Usuario o password invalidos");

		}

		return new User(usuario.getCorreo(), usuario.getPassword(), null);

	}

	@Override
	public Usuario actualizarUser(UserRegisterDTO registroDTO, long id) {

		Usuario usuario = new Usuario(id, registroDTO.getNombres(), registroDTO.getApellidos(),
				registroDTO.getDni(), registroDTO.getCorreo(),
				passwordEncoder.encode(registroDTO.getPassword()));

		return usuarioRepositorio.save(usuario);

	}

}
