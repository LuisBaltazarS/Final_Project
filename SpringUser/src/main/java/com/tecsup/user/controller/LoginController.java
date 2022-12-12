package com.tecsup.user.controller;

import org.springframework.beans.factory.annotation.Autowired; 
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import com.tecsup.user.model.Usuario;
import com.tecsup.user.repository.UserRepository;

@Controller
public class LoginController {
	
	@Autowired
	private UserRepository usuarioRepo;
	
	@GetMapping("/login")
	public String iniciarSesion() {
			
		return "login";
		
	}
	
	@GetMapping("/")
	public String PaginaInicio() {

		return "index";
		
	}
	
	@GetMapping("/perfil{username}")
	public String PaginaPerfil(@PathVariable("username") String username, Model model) {
		
		Usuario user = usuarioRepo.findByCorreo(username);
		model.addAttribute("usuario", user);
		
		return "perfil";
		
	}
	
	@GetMapping("/error")
	public String Errror() {
		
		return "error";
		
	}
	
	

}
