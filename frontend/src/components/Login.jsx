import React, { useState } from 'react';
import { login } from '../services/auth';

const Login = ({ history }) => {
  // Stato locale per username e password
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

  // Gestione del submit del form di login
    const handleSubmit = async (e) => {
    e.preventDefault();
    try {
        await login(username, password);
        history.push('/');
    } catch (err) {
        setError('Credenziali non valide');
    }
    };

    return (
    <div>
        <h2>Accedi</h2>
        <form onSubmit={handleSubmit}>
        <label>
            Nome utente:
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} required />
        </label><br />
        <label>
            Password:
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
        </label><br />
        <button type="submit">Accedi</button>
        {error && <p>{error}</p>}
        </form>
    </div>
    );
};

export default Login;
