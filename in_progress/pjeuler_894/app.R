library(ggplot2)
library(ggforce)
library(shiny)

ui <- fluidPage(
    sidebarLayout(
        sidebarPanel(
          sliderInput("x"     ,  "x"     , min = 2.4, max = 2.5, value = 2.474, step = 0.001),
          sliderInput("lambda",  "lambda", min = 0.9, max = 0.91, value = 0.906, step = 0.001),
          sliderInput("alpha" ,  "alpha" , min = 47, max = 48, value = 47.36, step = 0.01)
        ),
        mainPanel(plotOutput("distPlot"))
    )
)

server <- function(input, output) {

    output$distPlot <- renderPlot({
      
      n <- 20
      alpha0 <- input$alpha
      x <- input$x
      lambda <- input$lambda
      
      r0 <- x * lambda ^ seq(0,n)
      alpha <- alpha0 * seq(0,n) / 180 * pi
      
      x <- r0 * cos(alpha)
      y <- r0 * sin(alpha)
      r <- lambda ^ seq(0,n)
      
      df <- data.frame(x0=x,y0=y,r=r)
      
      df |> ggplot(aes(x0=x0,y0=y0,r=r)) + geom_circle()
    })
}
shinyApp(ui = ui, server = server)