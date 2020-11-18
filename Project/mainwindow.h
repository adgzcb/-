#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QImage>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();
    int globalMark;//儲存標記用
    QImage globalImg;//儲存圖片用

private slots:
    void on_ac_openfile_triggered();
    void on_ac_save_triggered();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H