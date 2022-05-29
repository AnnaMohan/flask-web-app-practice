function deleteNote(noteId) { //javaxscript method to send the get request to get the noteid
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }