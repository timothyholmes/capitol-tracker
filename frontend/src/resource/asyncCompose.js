
export default function compose (fxs) {
  return async (intialInput) => {
    let previousFunctionResult = intialInput
    for (const fx of fxs) {
      previousFunctionResult = await fx(previousFunctionResult)
    }
    return previousFunctionResult
  }
}
