
import axios from 'axios'

export default async function (endpoint) {
  try {
    const { data } = await axios.get(endpoint)

    return data
  } catch (e) {
    throw e
  }
}
