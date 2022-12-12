import React, { useState } from "react";
import "../components/css/register.css"

export const Register = (props) => {
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');
    const [name, setName] = useState('');
    const [surname, setSurname] = useState('');
    const [dni, setDni] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(email);
    }

    return (
        <div className="auth-form-container" id="image_register">
            <h2>Register</h2>
        <form className="register-form" onSubmit={handleSubmit}>
            <label htmlFor="name">Nombre</label>
            <input value={name} name="name" onChange={(e) => setName(e.target.value)} id="name" placeholder="nombre completo" />
            <label htmlFor="surname">Apellidos</label>
            <input value={surname} name="surname" onChange={(e) => setSurname(e.target.value)} id="surname" placeholder="apellidos" />
            <label htmlFor="dni">DNI</label>
            <input value={dni} name="dni" onChange={(e) => setDni(e.target.value)} id="dni" placeholder="número de dni" />
            <label htmlFor="email">Email</label>
            <input value={email} onChange={(e) => setEmail(e.target.value)}type="email" placeholder="@gmail.com" id="email" name="email" />
            <label htmlFor="password">Contraseña</label>
            <input value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="********" id="password" name="password" />
            <button type="submit">Login</button>
        </form>
        <button className="link-btn" onClick={() => props.onFormSwitch('login')}>No tienes una cuenta? Registrate aquí.</button>
    </div>
    )
}