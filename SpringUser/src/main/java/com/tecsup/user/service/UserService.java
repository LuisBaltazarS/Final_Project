package com.tecsup.user.service;

import com.tecsup.user.dto.UserRegisterDTO;
import com.tecsup.user.model.Usuario;

public interface UserService {
	
	public Usuario save(UserRegisterDTO usuario);
	
	

}
