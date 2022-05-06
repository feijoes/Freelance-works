import Lugar from '../Lugar'
const Center = () => {
    return `<div class='container main'>
                    ${Lugar("Roque Nublo, lugar de culto",
                    `Es la roca volcánica más identificable de Gran Canaria.
                    Con sus 80 metros de alto, esta mole se eleva a 1.813 metros sobre el nivel del mar.
                    Su origen se debe a una de las erupciones volcánicas que forjaron el archipiélago hace millones de años.
                    Lo más curioso del Roque Nublo es su vinculación con un lugar sagrado, un espacio de culto de los antiguos aborígenes.
                    Este es uno de los sitios que hay que visitar sí o sí en la isla.`,
                    "monte.jpg",1)}
                    ${Lugar("Dunas de Maspalomas, el pequeño desierto",
                    `Si no tienes una foto en las Dunas de Maspalomas, no has ido a Gran Canaria. 
                    Este desierto de Sahara en miniatura es uno de los paisajes más impactantes que tienes que visitar en la isla.
                    Recorre sus dunas, disfruta de las panorámicas y termina dándote un baño en las azules aguas del Atlántico.`,
                    "dunas.jpg",2)}      
                </div>`
};
export default Center