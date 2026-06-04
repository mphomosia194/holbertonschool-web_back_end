export default function cleanSet(set, startString) {
  if (!startString) {
    return '';
  }

  return [...set]
    .filter(
      (value) => typeof value === 'string'
      && value.startsWith(startString)
      && value.slice(startString.length) !== '',
    )
    .map((value) => value.slice(startString.length))
    .join('-');
}
