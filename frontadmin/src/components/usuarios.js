import React from 'react'

class Usuarios extends React.Component {

    constructor(props) {

        super(props);
    
        this.state = {
    
          usuarios: []
    
        }
      }
    
      componentWillMount() {
        fetch('http://localhost:8000/usuarios/')
          .then((response) => {
            return response.json()
          })
          .then((users) => {
            this.setState({ usuarios: users })
          })    
      } 

      render() {
        return (
          <div>
            <table border="1">
            <thead>
              <tr>
                <th>Código Usuario</th>
                <th>Nombres</th>
                <th>Apellidos</th>        
                <th>Fecha de Nacimiento</th> 
                <th>DNI</th>
                <th>Correo</th>
                <th>Contraseña</th>
                <th>Teléfono</th>
                <th>Tipo de Usuario</th>
                <th>Institución</th>
                <th>Tutor</th>            
              </tr>
            </thead>
            <tbody>  
              {this.state.usuarios.map(usuario => {
                return (
                  <tr key={usuario.id}>
                    <td>{usuario.nombres}</td>
                    <td>{usuario.apellidos}</td>
                    <td>{usuario.fecha_nac}</td>
                    <td>{usuario.dni}</td>
                    <td>{usuario.correo}</td>
                    <td>{usuario.password}</td>
                    <td>{usuario.telefono}</td>
                    <td>{usuario.tipo_id}</td>
                    <td>{usuario.institucion_id}</td>
                    <td>{usuario.tutor_id}</td>
                </tr>
                );
              })}
            </tbody>
            </table>
          </div>
        );
      }

}

export default Usuarios;