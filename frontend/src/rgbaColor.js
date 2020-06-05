
import { random } from 'lodash'

export class RGBA {
  constructor(r, g, b, a) {
    this.r = r || this.getRandomValue()
    this.g = g || this.getRandomValue()
    this.b = b || this.getRandomValue()
    this.a = a || this.getRandomValue()
  }

  getRandomValue() {
    return random(0, 255)
  }

  getString() {
    return `rgba(${this.r}, ${this.g}, ${this.b}, ${this.a})`
  }
}

export default {
  RGBA
}
