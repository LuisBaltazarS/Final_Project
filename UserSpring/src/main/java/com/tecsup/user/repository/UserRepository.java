package com.tecsup.user.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.tecsup.user.model.Usuario;

@Repository
public interface UserRepository extends CrudRepository<Usuario, Long>{

	
	
}

