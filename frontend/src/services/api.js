import axios from 'axios';
// Configurazione base dell'APi

const api = axios.create({
    baseURL: 'http://localhost:8000/api/',
});

//Intercettore per gestire l'autenticazione
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('accessToken')
        if (token) {
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
(error) => Promise.reject(error)
);

export default api