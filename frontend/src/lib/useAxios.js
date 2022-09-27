import axios from "axios";

const baseUrl = "//api.django.social/api/v1/";

const useAxios = () => {

    return axios.create({
        baseURL: baseUrl,
    })
}

export default useAxios;