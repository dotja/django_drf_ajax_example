  function job_type(job_type) {
    document.getElementById('location').value = '';
    let param = 'job_type='+ job_type;
    send_request(param);
  }

  function sort_jobs(sort_type) {
    document.getElementById('location').value = '';
    let param = 'sort_jobs='+ sort_type;
    send_request(param);
  }

  function find_location() {
    let location = document.getElementById('location').value;
    let param = 'location='+ location;
    send_request(param);
  }

  function send_request(param) {
    $.ajax({
      method: 'GET',
      url: 'api/get_jobs?' + param,
      beforeSend: function() {
        console.log('before send');
      },
      success: function(result) {
        update_table(result);
        console.log('after send');
      },
      error: function() {
        console.log('error');
      }
    });
  }


  function update_table(data) {
    let row;
    let all_rows = '';

    Object.keys(data).forEach(key => {
      elem = data[key];
      row = '<tr><td>' + elem['job_type'] + '</td>' + '<td>' + elem['location'] + '</td>' + '<td>' + elem['posted_on'] + '</td>' + '</tr>';
      all_rows = all_rows + row;
    });

    $('#myTable tbody').html(all_rows);
  }
