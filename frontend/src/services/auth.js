import api from "./api";
import jwtDecode from "jwt-decode";

// Funzione per effettuare il login
export const login  = async (username, password) => {
    const response  = await api.post('token/', {username, password});
    const {access, refresh} = response.data;
    localStorage.setItem('accessToken', access);
    localStorage.setItem('refreshToken', refresh);
    return jwtDecode(access);
};


// Funzione per effettuare il logout
export const logout = () => {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
};


//Funzione per verificare se l'utente è auutenticato
export const isAuthenticated = () => {
    const token = localStorage.getItem('accessToken');
    return !!token;
}