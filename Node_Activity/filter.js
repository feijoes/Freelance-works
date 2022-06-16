function filter(attraction, age, height) {
    if (attraction.Min_height) if (attraction.Min_height > height) return false
    if (attraction.Max_height) if (attraction.Max_height < height) return false
    if (attraction.Max_age) if (attraction.Max_age < age) return false
    if (attraction.Min_age) if (attraction.Min_age > age) return false
    return true;
}
export default filter