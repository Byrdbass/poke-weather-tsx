const capitalizeWords = (input: string) => {
    return input.split(" ")
    .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join(" ");
}

export { capitalizeWords }