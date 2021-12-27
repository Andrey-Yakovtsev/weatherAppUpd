import { createStore } from 'vuex'

export default createStore({
  state: {
    weatherQueries: {}
  },
  mutations: {
    setWeatherQueries (state, payload) {
      state.weatherQueries[`${payload.city_name}`] = payload.weather_data
    }
  },
  actions: {
  },
  modules: {
  }
})
