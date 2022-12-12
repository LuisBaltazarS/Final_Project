import React, { Component } from "react";
import "../components/css/login.css"
import axios from 'axios';

const baseUrl = "http://127.0.0.1:8000/administradores/";

class Login extends Component{
    
    state={

        form:{

            correo: '',
            password: ''

        }

    }

    handleChange=async e=>{

        await this.setState({

            form:{

                ...this.state.form,
                [e.target.name]: e.target.value

            }

        });

    }

    iniciarsesion=async()=>{

        await axios.get(baseUrl, {params: {correo: this.state.form.correo, password: this.state.form.password}})
        .then(response=>{
            
            console.log(response.data);
        
        })
        .catch(error=>{

            console.log(error);

        })

    }

    render(){

        return(
                <div className="auth-form-container" id="image_login"> 
                    <h2>Inicio de Sesión</h2>
                    <form className="login-form">
                        <label htmlFor="correo">Email</label>
                        <input  onChange={this.handleChange} type="email" placeholder="mail@gmail.com" id="design_input" name="correo" />
                        <label htmlFor="password">Contraseña</label>
                        <input onChange={this.handleChange} type="password" placeholder="********" id="design_input" name="password" />
                        <button type="submit" onClick={()=> this.iniciarsesion()}>Login</button>
                    </form>
                    <button className="link-btn" >No tienes una cuenta? Registrate aquí.</button>
                </div>

        )

    }
}

export default Login;