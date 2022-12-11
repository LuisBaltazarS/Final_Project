package com.tecsup.user.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class LoginController {
	
	@GetMapping("/login")
	public String iniciarSesion() {
		
		return "login";
		
	}
	
	@GetMapping("/")
	public String PaginaInicio() {
		
		return "index";
		
	}
	
	

}
