import React, { useState } from "react";
import "./Login.css"

export const Login = (props) => {
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(email);
    }

    return (
        <div className="auth-form-container" id="image_login"> 
            <h2>Inicio de Sesión</h2>
            <form className="login-form" onSubmit={handleSubmit}>
                <label htmlFor="email">Email</label>
                <div class="input-group flex-nowrap">
                <input  class="form-control" placeholder="Username" aria-label="Username" aria-describedby="addon-wrapping"></input>
                </div>
                <input value={email} onChange={(e) => setEmail(e.target.value)}type="email" placeholder="mail@gmail.com" id="design_input" name="email" />
                <label htmlFor="password">Contraseña</label>
                <input value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="********" id="design_input" name="password" />
                <button type="submit">Login</button>
            </form>
            <button className="link-btn" onClick={() => props.onFormSwitch('register')}>No tienes una cuenta? Registrate aquí.</button>
        </div>
    )
}