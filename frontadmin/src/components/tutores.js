import React from 'react'

class Tutores extends React.Component {

  constructor(props) {

    super(props);

    this.state = {

      usuarios: []

    }
  }

  componentWillMount() {
    fetch('http://localhost:8000//')
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
        <table className="table">
        <thead>
          <tr>
            <th scope="col">Código Usuario</th>
            <th scope="col">Nombres</th>
            <th scope="col">Apellidos</th>        
            <th scope="col">Fecha de Nacimiento</th> 
            <th scope="col">DNI</th>
            <th scope="col">Correo</th>
            <th scope="col">Contraseña</th>
            <th scope="col">Teléfono</th>
            <th scope="col">Tipo de Usuario</th>
            <th scope="col">Institución</th>
            <th scope="col">Tutor</th>            
          </tr>
        </thead>
        <tbody>  
          {this.state.usuarios.map(usuario => {
            return (
              <tr scope="row" key={usuario.id}>
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

export default Tutores;