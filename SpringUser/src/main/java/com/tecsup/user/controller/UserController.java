package com.tecsup.user.controller;

import java.util.Optional;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;

import com.tecsup.user.dto.UserRegisterDTO;
import com.tecsup.user.model.Usuario;
import com.tecsup.user.service.UserService;

@Controller
@RequestMapping("/registro")
public class UserController {

	private UserService userService;
	
	public UserController(UserService userService) {
		super();
		this.userService = userService;
	}
	
	@ModelAttribute("usuario")
	public UserRegisterDTO returnUser() {
		
		return new UserRegisterDTO();
		
	}
	
	@GetMapping
	public String mostrarForm() {
		
		return "Modelo_register";
		
	}
	
	@PostMapping
	public String registrarCuenta(@ModelAttribute("usuario") UserRegisterDTO registroDTO) {
		userService.save(registroDTO);
		return "redirect:/registro?exito";
		
	}
	
	@GetMapping(path = "/{id}")
	public Optional<Usuario> UserfindByCorreo(@PathVariable("id") Long id) {
		
		return userService.getUserById(id);
		
	}
	
	@DeleteMapping(path = "/{id}")
	public String deleteUserById(@PathVariable("id") Long id) {
		
		boolean ok = userService.deleteUser(id);
		
		if(ok) {
			
			return "Se elimino el usuario con el id " + id;
			
		}else {
			
			return "No se pudo eliminar al usuario con el id " + id;
			
		}
		
	}
	
	@PutMapping(path = "/{id}")
	public Usuario actualizarUser(@RequestBody UserRegisterDTO registroDTO, @PathVariable("id") Long id) {
		
		return userService.actualizarUser(registroDTO, id);
		
	}
	
}


















