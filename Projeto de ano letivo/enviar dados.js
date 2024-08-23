function doPost(e) {
    try {
      // Verificar se a requisição contém dados
      if (!e.postData || !e.postData.contents) {
        return ContentService.createTextOutput("Nenhum dado recebido.");
      }
  
      // Tentar fazer o parsing dos dados como JSON
      var params = JSON.parse(e.postData.contents);
      
      // Pegar a pasta no Google Drive (substitua pelo ID da pasta onde deseja salvar)
      var folder = DriveApp.getFolderById('1fkhZNCYCaCyKIay7P5VRuoA16mXVoEay');
      
      // Criar um nome único para o arquivo com base no tempo atual
      var timestamp = new Date().toISOString();
      var fileName = 'dados_recebidos_' + timestamp + '.txt';
      
      // Criar um arquivo e salvar os dados formatados como JSON
      var file = folder.createFile(fileName, JSON.stringify(params, null, 2));
      
      // Retornar resposta de sucesso
      return ContentService.createTextOutput("Dados recebidos e salvos no Google Drive.");
    } catch (error) {
      // Em caso de erro, retornar uma resposta de erro
      return ContentService.createTextOutput("Erro ao processar os dados: " + error.message);
    }
  }