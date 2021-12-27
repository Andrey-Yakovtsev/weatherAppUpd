<template>
  <div class="section-main__title">
    Show me the weather
  </div>
  <button class="section-button" @click="getGEO">
    By my location
  </button>
  <div class="section-main__subtitle">
    or
  </div>
  <div>
    <input v-model="cityName" placeholder="By city name" @keydown.enter="makeAPICallByCity"/>
    <button class="section-button" @click="makeAPICallByCity">
      Show
    </button>
  </div>
  <div>
    <div class="result" v-if="weatherFetchResult">
      {{weatherFetchResult}}
    </div>
    <div v-if="lookupError" class="section-main__error">
      {{lookupError}}
    </div>
    <div class="section-main__subtitle">
      Your recent searches:
      <div>
        <button class="section-button__badge" v-for="city in queriesList" :key="city.city_name">
          {{city.name}}
        </button>
      </div>
    </div>
  </div>

</template>

<script>
import { computed, reactive, ref } from 'vue'
import { useStore } from 'vuex'
import axios from 'axios'

export default {
  name: 'index',
  setup () {
    const lookupError = ref(null)
    const store = useStore()
    const showSpinner = ref(false)
    const cityName = ref('')
    let coords = reactive({})
    const apikey = ref('4894b527cae585bef8e05223b5a54412')
    const weatherFetchResult = ref(null)

    const queriesList = computed(() => store.state.weatherQueries)

    function getGEO () {
      const getLocationData = new Promise((resolve) => {
        getCurrentGeoLocation()
        resolve(coords)
        getLocationData.then(
        )
        // eslint-disable-next-line no-unused-expressions
          .catch((error) => { error.message })
      }
      )
    }

    function saveQueryToStore (data) {
      // eslint-disable-next-line prefer-const
      let weatherQuery = {
        city_name: data.name,
        weather_data: data
      }
      store.commit('setWeatherQueries', weatherQuery)
      postQueryToDB()
    }

    function postQueryToDB () {
      axios.post(
        'http://127.0.0.1:8000/api/weatherapi/',
        {
          city_name: weatherFetchResult.value.name,
          weather_data: weatherFetchResult.value
        }
      )
        .then(() => {
        }).catch((error) => {
          console.log(error.message)
        })
    }

    function getCurrentGeoLocation () {
      if ('geolocation' in navigator) {
        navigator.geolocation.getCurrentPosition(function (position) {
          coords = { latitude: position.coords.latitude, longitude: position.coords.longitude }
          makeAPICallByGeo()
        })
      } else {
        lookupError.value = 'Location service is not supported by browser'
      }
    }

    function makeAPICallByCity () {
      axios.get(`https://api.openweathermap.org/data/2.5/weather?q=${cityName.value}&appid=${apikey.value}`).then(
        (response) => {
          weatherFetchResult.value = response.data
          saveQueryToStore(response.data)
        }).catch(() => {
        lookupError.value = 'No such city in our DB. Try another'
      })
    }

    function makeAPICallByGeo () {
      axios.get(`https://api.openweathermap.org/data/2.5/weather?lat=${coords.latitude}&lon=${coords.longitude}&appid=${apikey.value}`).then(
        (response) => {
          weatherFetchResult.value = response.data
          saveQueryToStore(response.data)
        }).catch((error) => {
        console.warn(error.message)
      })
    }

    return {
      lookupError,
      queriesList,
      showSpinner,
      coords,
      cityName,
      makeAPICallByCity,
      weatherFetchResult,
      getGEO
    }
  }
}
</script>

<style scoped lang="scss">
input {
  width: 50%;
  font-family: 'Noto Sans', sans-serif;
  font-size: 1.4rem;
  color: black;
  font-weight: 400;
  padding: 1rem 0;
  outline: none;
  border: none;
  border-bottom: 1px solid #9D9D9D;
}
.section-button {
  position: relative;
  align-items: center;
  justify-content: center;
  padding: 0.5rem 0.5rem;
  margin: 1rem 1rem;
  font-size: 1.75rem;
  outline: none;
  transition: all .2s;
  height: 4.5rem;
  min-width: 20rem;

  &__badge {
    font-size: 0.75rem;
    height: 1.5rem;
    min-width: 10rem;
    margin: 10px;
  }
}
.section-main {
  height: 50vh;
  max-height: 48rem;

  &__title {
    margin: 0 auto 4rem;
    font-family: 'Noto Sans', sans-serif;
    text-align: center;
    color: #00b471;
    font-size: 2rem;
    text-transform: uppercase;
    font-weight: 600;
  }
  &__subtitle {
    margin: 0 auto 4rem;
    font-family: 'Noto Sans', sans-serif;
    text-align: center;
    color: #00b471;
    font-size: 2rem;
    text-transform: uppercase;
    font-weight: 600;
  }
  &__error {
    margin: 0 auto 4rem;
    font-family: 'Noto Sans', sans-serif;
    text-align: center;
    color: #ff0000;
    font-size: 1rem;
    text-transform: uppercase;
    font-weight: 600;
  }
}

</style>
