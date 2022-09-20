#include "MainWindow.h"
#include "ui_MainWindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}




void MainWindow::on_pushButton_ResetMap_clicked()
{

}


void MainWindow::on_pushButton_AStarCal_clicked()
{

}


void MainWindow::on_pushButton_GreedCal_clicked()
{

}


void MainWindow::on_doubleSpinBox_valueChanged(double arg1)
{

}

