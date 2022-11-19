// Adapted from Christopher Martin on StackOverflow (CC-BY-SA 4.0): https://stackoverflow.com/a/70062967/7414541

// open closed details elements for printing
window.addEventListener('beforeprint',() =>
{
    const allDetails = document.body.querySelectorAll('details');
    for(let details of allDetails)
    {
        if(details.open)
        {
            details.dataset.open = '1';
        }
        else
        {
            details.setAttribute('open', '');
        }

        let summaryTag = details.querySelector("summary");
        let summaryText = summaryTag.textContent;
        let newSummaryText = summaryText.replace("Klikk her", "Se under")
        summaryTag.textContent = newSummaryText;

    }
});

// after printing close details elements not opened before
window.addEventListener('afterprint',() =>
{
    const allDetails = document.body.querySelectorAll('details');
    for(let details of allDetails)
    {
        if(details.dataset.open)
        {
            details.dataset.open = '';
        }
        else
        {
            details.removeAttribute('open');
        }

        let summaryTag = details.querySelector("summary");
        let summaryText = summaryTag.textContent;
        let newSummaryText = summaryText.replace("Se under", "Klikk her")
        summaryTag.textContent = newSummaryText;

    }
});