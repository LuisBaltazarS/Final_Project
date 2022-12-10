package com.tecsup.user.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.tecsup.user.dto.UserRegisterDTO;
import com.tecsup.user.service.UserService;

@Controller
@RequestMapping("/registro")
public class UserController {

	private UserService userService;
	
	@ModelAttribute("usuario")
	public UserRegisterDTO retornoNewUser() {
		
		return new UserRegisterDTO();
		
	}
	
	@GetMapping
	public String formRegister() {
		
		return "registro";
		
	}
	
	@PostMapping
	public String registrarCuenta(@ModelAttribute("usuario") UserRegisterDTO registroDTO) {
		
		userService.save(registroDTO);
		
		return "redirect:/registro?exito"; 
		
	}
	
}
